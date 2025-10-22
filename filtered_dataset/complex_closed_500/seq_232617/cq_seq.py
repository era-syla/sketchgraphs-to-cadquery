import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.03372, 0.00177).lineTo(-0.04238, 0.00177).lineTo(-0.04238, -0.00177).lineTo(-0.03372, -0.00177).lineTo(-0.03372, 0.00177).close()
solid=wp_sketch0.add(loop0).extrude(0.02350235636136893)
