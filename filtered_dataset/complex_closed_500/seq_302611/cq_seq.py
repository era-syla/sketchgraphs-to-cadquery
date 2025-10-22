import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.04, 0.365).lineTo(2.715, 0.365).lineTo(2.715, 0.448).lineTo(0.04, 0.448).lineTo(0.04, 0.365).close()
solid=wp_sketch0.add(loop0).extrude(-7.325340463234064)
