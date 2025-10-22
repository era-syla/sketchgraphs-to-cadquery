import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00294, 0.02537).lineTo(-0.0889, 0.02537).lineTo(-0.0889, 0.02696).lineTo(-0.00294, 0.02696).lineTo(-0.00294, 0.02537).close()
solid=wp_sketch0.add(loop0).extrude(0.026643343004911623)
