
clc; clear all; close all;

N = 4;
x = zeros(N,N);
x(1:N/2, 1:N/2) = 1


h = figure();
imagesc(x);
saveas(h, 'simulation.png', 'jpeg')
%drawnow()
