import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0293, 0.03179).lineTo(0.04339, 0.03179).lineTo(0.04339, -0.04795).lineTo(-0.0293, -0.04795).lineTo(-0.0293, 0.03179).close()
solid=wp_sketch0.add(loop0).extrude(-0.12897092994091558)
