import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.006, 0.046).lineTo(0.07, 0.046).lineTo(0.07, 0.0).lineTo(0.006, 0.0).lineTo(0.006, 0.046).close()
solid=wp_sketch0.add(loop0).extrude(-0.15567714443865407)
