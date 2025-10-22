import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.12485, 0.0127).lineTo(-0.12485, 0.01321).lineTo(-0.12371, 0.0127).lineTo(-0.12485, 0.0127).close()
solid=wp_sketch0.add(loop0).extrude(0.0014612285318683703)
