# MasterX Study Android (GitHub APK build)

This repository wraps the supplied `index.html` as an Android app using Capacitor.
GitHub Actions builds a **debug APK** automatically when you push to `main`, or when
you manually run the workflow.

## Create the GitHub repository

1. Create a new **empty** repository on GitHub (for example `masterx-android`).
2. Upload the contents of this ZIP to the repository root (not the ZIP file itself).
3. Commit the files to the `main` branch.
4. Open the repository's **Actions** tab.
5. Select **Build MasterX APK** and press **Run workflow**, or wait for the push build.
6. Open the completed workflow run, scroll to **Artifacts**, and download
   `MasterX-Study-debug-apk`. Extract it to get `app-debug.apk`.
7. Install the APK on your Android phone. If Android asks, allow installation
   from that source.

## Important: backend/API features

The supplied HTML contains requests to relative Flask endpoints such as `/api/me`,
`/api/csrf`, `/api/notifications`, `/api/google-login`, and `/add_task`. The uploaded
file does **not** include the Flask server/backend. In a locally bundled APK those
server features will not work until the existing backend is deployed to HTTPS and
the frontend API requests are configured to use that backend URL (including CORS,
cookies/CSRF and Google OAuth settings). Features that rely only on the page and
browser local storage can still run.

The HTML also has an optional online chat whose Firebase database URL is blank by
default. Configure a Firebase Realtime Database URL and its security rules before
expecting online chat to work.

## App identity and icon

- Android package ID: `com.masterx.study`
- Display name: `MasterX Study`
- The included `www/static/icon-192.png` is a simple placeholder icon. Replace it
  with your official MasterX icon if you have one.

## Build type

This workflow produces an unsigned **debug APK** for testing/sideloading. It is not
a signed release APK for Play Store publishing.
