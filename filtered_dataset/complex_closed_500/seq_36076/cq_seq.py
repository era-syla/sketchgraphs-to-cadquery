import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, -0.00156).lineTo(-0.007, -0.00156).lineTo(-0.007, 0.00244).lineTo(-0.003, 0.01404).lineTo(0.0, 0.01404).lineTo(0.0, -0.00156).close()
solid=wp_sketch0.add(loop0).extrude(-0.04313888716158825)
