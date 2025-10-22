import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.3, 0.0).lineTo(0.3, 0.6).lineTo(-0.0, 0.6).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-1.592945858360284)
