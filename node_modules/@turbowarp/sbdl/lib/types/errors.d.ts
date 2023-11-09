export class HTTPError extends Error {
    /**
     * @param {string} url
     * @param {number} status HTTP status
     */
    constructor(url: string, status: number);
    url: string;
    status: number;
}
export class CanNotAccessProjectError extends Error {
    constructor(message: any);
}
/**
 * NOTE: Do NOT use `instanceof AbortError` to detect abort errors.
 * Use `error.name === 'AbortError'` instead.
 */
export class AbortError extends Error {
    constructor(message: any);
}
