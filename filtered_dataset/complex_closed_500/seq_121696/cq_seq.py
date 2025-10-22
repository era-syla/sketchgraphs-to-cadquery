import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.03493, 0.15113).lineTo(-0.01588, 0.15113).lineTo(-0.01588, 0.16383).lineTo(-0.03493, 0.16383).lineTo(-0.03493, 0.15113).close()
solid=wp_sketch0.add(loop0).extrude(-0.005465542667985484)
