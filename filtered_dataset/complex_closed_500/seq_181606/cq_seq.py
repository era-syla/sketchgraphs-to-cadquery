import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.02119, 0.02185).lineTo(-0.00363, 0.02185).lineTo(-0.00363, -0.01271).lineTo(-0.02119, -0.01271).lineTo(-0.02119, 0.02185).close()
solid=wp_sketch0.add(loop0).extrude(-0.07146313664884764)
