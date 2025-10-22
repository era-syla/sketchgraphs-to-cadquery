import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.075, -0.0135).lineTo(0.075, -0.0135).lineTo(0.075, -0.0105).lineTo(-0.075, -0.0105).lineTo(-0.075, -0.0135).close()
solid=wp_sketch0.add(loop0).extrude(-0.12161042851284054)
