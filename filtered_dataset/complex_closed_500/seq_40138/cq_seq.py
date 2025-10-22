import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.02078, -0.04).lineTo(0.15935, -0.04).lineTo(0.15935, -0.03).lineTo(-0.02078, -0.03).lineTo(-0.02078, -0.04).close()
solid=wp_sketch0.add(loop0).extrude(0.5268135016585459)
