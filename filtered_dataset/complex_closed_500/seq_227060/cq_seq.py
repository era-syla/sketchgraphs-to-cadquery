import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.008, 0.0).lineTo(0.008, 0.0).lineTo(0.0054, -0.00524).lineTo(0.0029, -0.0065).lineTo(-0.0029, -0.0065).lineTo(-0.0054, -0.00524).lineTo(-0.008, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.008180966441694125)
