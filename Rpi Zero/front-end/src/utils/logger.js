const isDev = process.env.NODE_ENV !== 'production';

const logger = {
  log(...args) {
    if (!isDev) {
      return; // guard
    }
    console.log(args);
  },

  info(...args) {
    if (!isDev) {
      return; // guard
    }
    console.info(args);
  },

  error(...args) {
    if (!isDev) {
      return; // guard
    }
    console.error(args);
  },

  time(...args) {
    if (!isDev) {
      return; // guard
    }
    console.time(args);
  },

  timeEnd(...args) {
    if (!isDev) {
      return; // guard
    }
    console.timeEnd(args);
  },
};

export default logger;
