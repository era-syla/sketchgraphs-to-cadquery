import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.325, 0.0).lineTo(0.125, -0.4).lineTo(0.325, -0.4).lineTo(0.325, -0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.15237772210043127)
