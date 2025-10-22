import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.07303, 0.32702).lineTo(-0.03493, 0.32702).lineTo(-0.03493, 0.25082).lineTo(-0.07303, 0.25082).lineTo(-0.07303, 0.32702).close()
solid=wp_sketch0.add(loop0).extrude(-0.060310437246730984)
