import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(3.71, -3.33).lineTo(2.37, -3.33).lineTo(2.37, -1.17).lineTo(3.71, -1.17).lineTo(3.71, -3.33).close()
solid=wp_sketch0.add(loop0).extrude(6.21155568842117)
