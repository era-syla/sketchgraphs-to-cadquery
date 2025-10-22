import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.10027, -0.10036).lineTo(-0.09973, -0.10036).lineTo(-0.09973, 0.09964).lineTo(0.10027, 0.09964).lineTo(0.10027, -0.10036).close()
solid=wp_sketch0.add(loop0).extrude(-0.07122128299904577)
