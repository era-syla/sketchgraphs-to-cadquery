import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.02547, 0.01264).lineTo(-0.02676, 0.00612).lineTo(-0.02798, 0.00621).lineTo(-0.02979, 0.00835).lineTo(-0.03193, 0.00654).lineTo(-0.03314, 0.00665).lineTo(-0.03256, 0.01326).lineTo(-0.03135, 0.01315).lineTo(-0.03182, 0.00777).lineTo(-0.02969, 0.00958).lineTo(-0.02776, 0.00731).lineTo(-0.02666, 0.01287).lineTo(-0.02547, 0.01264).close()
solid=wp_sketch0.add(loop0).extrude(0.020731621390951777)
