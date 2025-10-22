import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.01333, 0.03031).lineTo(0.01905, 0.03031).lineTo(0.01905, -0.00271).lineTo(0.01333, -0.00271).lineTo(0.01333, 0.03031).close()
solid=wp_sketch0.add(loop0).extrude(0.03503889511112074)
