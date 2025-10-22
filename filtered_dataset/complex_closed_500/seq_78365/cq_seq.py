import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.01501).lineTo(0.05923, 0.01501).lineTo(0.05923, -0.04709).lineTo(0.0, -0.04709).lineTo(0.0, 0.01501).close()
solid=wp_sketch0.add(loop0).extrude(0.09179638568928357)
