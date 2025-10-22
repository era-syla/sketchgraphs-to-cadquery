import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.013, -0.00748).lineTo(-0.013, -0.00748).lineTo(-0.013, 0.02852).lineTo(0.013, 0.02852).lineTo(0.013, -0.00748).close()
solid=wp_sketch0.add(loop0).extrude(-0.020319475604080907)
