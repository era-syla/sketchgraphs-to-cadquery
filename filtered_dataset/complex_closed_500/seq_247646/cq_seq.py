import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.07673, 0.13284).lineTo(0.05015, 0.13284).lineTo(0.05015, 0.13614).lineTo(0.08051, 0.13614).threePointArc((0.08018, 0.13602), (0.08001, 0.1357)).threePointArc((0.07891, 0.13366), (0.07673, 0.13284)).close()
solid=wp_sketch0.add(loop0).extrude(0.020797775577423256)
