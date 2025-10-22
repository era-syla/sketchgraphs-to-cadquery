import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.145, 0.135).lineTo(-0.145, 0.135).lineTo(-0.145, -0.135).lineTo(0.145, -0.135).lineTo(0.145, 0.135).close()
solid=wp_sketch0.add(loop0).extrude(-0.2960164760741122)
