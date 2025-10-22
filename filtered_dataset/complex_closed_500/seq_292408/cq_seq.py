import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.00282, 0.0).lineTo(0.00275, 0.0).lineTo(0.00275, 0.00114).lineTo(0.00161, 0.00114).lineTo(0.00161, 0.00265).lineTo(-0.00169, 0.00265).lineTo(-0.00169, 0.00114).lineTo(-0.00282, 0.00114).lineTo(-0.00282, -0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.0032016994751078807)
