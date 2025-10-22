import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.71524, 0.0).lineTo(-0.74424, 0.0).lineTo(-0.74424, 0.028).lineTo(-0.71524, 0.028).lineTo(-0.71524, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.02511925139877168)
