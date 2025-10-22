import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.16758, 0.0).lineTo(-0.16758, 0.01822).lineTo(-0.13878, 0.01822).lineTo(-0.13878, 0.03486).lineTo(-0.0812, 0.03486).lineTo(-0.0812, 0.02857).lineTo(-0.07175, 0.02857).lineTo(-0.07175, 0.03486).lineTo(-0.04167, 0.03486).lineTo(-0.04167, 0.05208).lineTo(-0.02947, 0.05208).lineTo(-0.02947, 0.01822).lineTo(0.0, 0.01822).lineTo(0.0, 0.0).lineTo(-0.16758, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.3090502477165864)
