import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.03055).lineTo(0.03606, 0.03055).lineTo(0.03606, 0.05621).lineTo(0.05612, 0.05621).lineTo(0.05612, 0.07077).lineTo(0.06819, 0.07077).lineTo(0.06819, 0.0).lineTo(0.0, 0.0).lineTo(0.0, 0.03055).close()
solid=wp_sketch0.add(loop0).extrude(-0.03263634979352017)
