export default fetchAsArrayBufferWithProgress;
/**
 * @param {stirng} url
 * @param {(progress: number) => void} progressCallback
 * @param {AbortSignal} [abortSignal]
 * @returns {Promise<ArrayBuffer>}
 */
declare function fetchAsArrayBufferWithProgress(url: stirng, progressCallback: (progress: number) => void, abortSignal?: AbortSignal): Promise<ArrayBuffer>;
