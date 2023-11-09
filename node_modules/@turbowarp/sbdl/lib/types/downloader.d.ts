export function downloadProjectFromJSON(projectData: object, options?: Options): Promise<DownloadedProject>;
export function downloadProjectFromBuffer(data: ArrayBuffer | ArrayBufferView, options?: Options): Promise<DownloadedProject>;
export function getProjectMetadata(id: string, options?: Options): Promise<ProjectMetadata>;
export function downloadProjectFromURL(url: string, options?: Options): Promise<DownloadedProject>;
export function downloadProjectFromID(id: string, options?: Options): Promise<DownloadedProject>;
export function downloadLegacyProjectFromID(id: string, options?: Options): Promise<DownloadedProject>;
export type ProjectType = 'sb' | 'sb2' | 'sb3';
export type DownloadedProject = {
    title: string;
    type: ProjectType;
    arrayBuffer: ArrayBuffer;
};
export type Options = {
    /**
     * Called periodically with progress updates.
     */
    onProgress?: (type: 'project' | 'assets' | 'compress', loaded: number, total: number) => void;
    /**
     * The date to use for the "last modified" time in generated projects. If not set, defaults to an arbitrary date in the past.
     */
    date?: Date;
    /**
     * Whether to compress generated projects or not. Compressed projects take longer to generate but are much smaller. Defaults to true.
     */
    compress?: boolean;
    /**
     * An AbortSignal that can be used to cancel the download.
     */
    signal?: AbortSignal;
    /**
     * The URL from which to download assets from. $id is replaced with the asset ID (md5ext).
     */
    assetHost?: string;
    /**
     * Called during the download to access project.json. Return an object to replace project.json.
     */
    processJSON?: (type: ProjectType, data: unknown) => unknown | Promise<unknown>;
};
export type InternalProgressTarget = {
    fetching: (md5ext: string) => void;
    fetched: (md5ext: string) => void;
};
export type SB3Project = {
    targets: SB3Target[];
};
export type SB3Target = {
    sounds: SB3Asset[];
    costumes: SB3Asset[];
};
/**
 * Raw costume or sound data from an sb3 project.json.
 */
export type SB3Asset = {
    /**
     * md5 checksum of the asset (eg. b7b7898cfcd9ba13e89a4e74dd56a1ff)
     */
    assetId: string;
    /**
     * file extension of the asset (eg. svg, wav)
     */
    dataFormat: string;
    /**
     * dataFormat (eg. b7b7898cfcd9ba13e89a4e74dd56a1ff.svg)
     * md5ext is not guaranteed to exist.
     * There are additional properties that we don't care about.
     */
    md5ext: string | undefined;
};
export type ProjectMetadata = {
    id: number;
    title: string;
    description: string;
    instructions: string;
    visibility: string;
    public: boolean;
    comments_allowed: boolean;
    is_published: boolean;
    author: {
        id: number;
        username: string;
        scratchteam: boolean;
        history: {
            joined: string;
        };
        profile: {
            id: null;
            images: Record<'90x90' | '60x60' | '55x55' | '50x50' | '32x32', string>;
        };
    };
    image: string;
    images: Record<'282x218' | '216x163' | '200x200' | '144x108' | '135x102' | '100x80', string>;
    history: {
        created: string;
        modified: string;
        shared: string;
    };
    stats: {
        views: number;
        loves: number;
        favorites: number;
        remixes: number;
    };
    remix: {
        parent: number | null;
        root: number | null;
    };
    project_token: string;
};
