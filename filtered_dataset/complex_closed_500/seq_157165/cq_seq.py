import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.02367, -0.04723).lineTo(-0.01015, -0.0689).lineTo(-0.02657, -0.0689).lineTo(-0.02367, -0.04723).close()
solid=wp_sketch0.add(loop0).extrude(-0.0119921688265526)
