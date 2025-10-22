import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(2.175, -2.77).lineTo(2.085, -2.77).lineTo(2.085, -0.06).lineTo(2.175, -0.06).lineTo(2.175, -2.77).close()
solid=wp_sketch0.add(loop0).extrude(0.886069137534675)
