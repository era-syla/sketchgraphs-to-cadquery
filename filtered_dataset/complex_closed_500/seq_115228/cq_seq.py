import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.02413, 0.03211).lineTo(-0.0271, 0.03211).lineTo(-0.0271, -0.02996).lineTo(-0.02413, -0.02996).lineTo(-0.02413, 0.03211).close()
solid=wp_sketch0.add(loop0).extrude(-0.008156327638472462)
