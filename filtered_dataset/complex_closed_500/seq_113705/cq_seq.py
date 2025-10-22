import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.4191, 0.9779).lineTo(0.42228, 0.9779).lineTo(0.42228, 0.9271).lineTo(0.4191, 0.9271).lineTo(0.4191, 0.9779).close()
solid=wp_sketch0.add(loop0).extrude(0.0491775871140928)
