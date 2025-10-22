import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.01532, 0.0).lineTo(0.03741, 0.0).lineTo(0.03741, 0.04053).lineTo(0.01532, 0.04053).lineTo(0.01532, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.01376952698460907)
