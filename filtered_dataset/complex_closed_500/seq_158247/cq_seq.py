import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.18024, 0.21077).lineTo(0.22024, 0.21077).lineTo(0.22024, 0.17077).lineTo(0.18024, 0.17077).lineTo(0.18024, 0.21077).close()
solid=wp_sketch0.add(loop0).extrude(-0.016117021764314256)
