import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.07794, 0.13578).lineTo(-0.09386, 0.13578).lineTo(-0.09386, 0.14363).lineTo(-0.07794, 0.14363).lineTo(-0.07794, 0.13578).close()
solid=wp_sketch0.add(loop0).extrude(-0.004245619931324217)
