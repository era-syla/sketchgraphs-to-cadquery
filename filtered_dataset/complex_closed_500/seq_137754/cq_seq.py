import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.01325, 0.0645).lineTo(0.01325, 0.0645).lineTo(0.01325, 0.0245).lineTo(-0.01325, 0.0245).lineTo(-0.01325, 0.0645).close()
solid=wp_sketch0.add(loop0).extrude(0.06615871210938618)
