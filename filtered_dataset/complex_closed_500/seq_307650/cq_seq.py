import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.1493, -0.14334).lineTo(-0.1507, -0.14334).lineTo(-0.1507, 0.10666).lineTo(0.1493, 0.10666).lineTo(0.1493, -0.14334).close()
solid=wp_sketch0.add(loop0).extrude(0.23682501361171715)
