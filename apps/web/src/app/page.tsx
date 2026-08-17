export default function Home() {
  return (
    <main className="flex min-h-screen items-center justify-center px-6 py-16">
      <section
        aria-labelledby="page-title"
        className="w-full max-w-2xl rounded-2xl border border-slate-200 bg-white p-8 shadow-sm sm:p-12"
      >
        <p className="mb-4 text-sm font-semibold tracking-wider text-blue-700 uppercase">
          Sprint 00
        </p>
        <h1
          id="page-title"
          className="text-4xl font-bold tracking-tight text-slate-950 sm:text-5xl"
        >
          Financial Pods
        </h1>
        <p className="mt-5 max-w-xl text-lg leading-8 text-slate-600">
          The development foundation is running. Product experiences are
          intentionally deferred to an approved future sprint.
        </p>
        <p
          role="status"
          className="mt-8 inline-flex rounded-full bg-emerald-50 px-4 py-2 text-sm font-medium text-emerald-800"
        >
          Web service operational
        </p>
      </section>
    </main>
  );
}
