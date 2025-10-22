import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.06, 0.06).lineTo(-0.04, 0.06).lineTo(-0.04, 0.02).lineTo(-0.06, 0.02).lineTo(-0.06, 0.06).close()
solid=wp_sketch0.add(loop0).extrude(0.09319644578554458)
