import type { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.drivehenrico.app',
  appName: 'DriveHenrico',
  webDir: 'dist',
  plugins: {
    CapacitorCookies: {
      enabled: true,
    }
  }
};

export default config;
