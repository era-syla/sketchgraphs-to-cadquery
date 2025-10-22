import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.03508, 0.0566).lineTo(-0.02469, 0.0566).lineTo(0.0123, 0.01352).lineTo(0.0123, 0.00418).lineTo(-0.03507, 0.00418).lineTo(-0.03508, 0.0566).close()
solid=wp_sketch0.add(loop0).extrude(0.10576635458931555)
