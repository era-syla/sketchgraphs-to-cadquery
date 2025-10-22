import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0625, -0.0225).lineTo(-0.0625, -0.0225).lineTo(-0.0625, 0.0225).lineTo(0.0625, 0.0225).lineTo(0.0625, -0.0225).close()
solid=wp_sketch0.add(loop0).extrude(-0.13721000868101668)
