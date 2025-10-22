import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.66236, 0.4572).lineTo(0.55684, 0.4572).lineTo(0.55684, -0.4572).lineTo(-0.66236, -0.4572).lineTo(-0.66236, 0.4572).close()
solid=wp_sketch0.add(loop0).extrude(-0.7540030845617335)
