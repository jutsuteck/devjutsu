import type { AppProps } from "next/app";
import { QueryClient, QueryClientProvider } from "react-query";
import { Questrial } from "next/font/google";

import "@/styles/globals.css";

const queryClient = new QueryClient();

const questrial = Questrial({ subsets: ["latin"], weight: ["400"] });

const App = ({ Component, pageProps }: AppProps) => {
  return (
    <QueryClientProvider client={queryClient}>
      <main className={questrial.className}>
        <Component {...pageProps} />
      </main>
    </QueryClientProvider>
  );
};

export default App;
