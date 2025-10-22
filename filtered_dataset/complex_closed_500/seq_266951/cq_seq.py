import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.02753, 0.01622).lineTo(0.02247, 0.01622).lineTo(0.02247, -0.03378).lineTo(-0.02753, -0.03378).lineTo(-0.02753, 0.01622).close()
solid=wp_sketch0.add(loop0).extrude(-0.02171912305699175)
