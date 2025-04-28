'use client'
import React from "react";
import Image from "next/image";
import { useRouter } from 'next/navigation';

export default function Home() {
  const router = useRouter(); // Move useRouter inside the functional component

  // Use a side effect to handle navigation
  React.useEffect(() => {
    router.push('/dashboard'); // Correct the router usage
  }, [router]);

  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      hi there
    </div>
  );
}