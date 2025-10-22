import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00462, -0.00499).lineTo(0.01438, -0.00499).lineTo(0.01438, -0.00399).lineTo(-0.00362, -0.00399).lineTo(-0.00362, 0.01401).lineTo(-0.00462, 0.01401).lineTo(-0.00462, -0.00499).close()
solid=wp_sketch0.add(loop0).extrude(0.023111569824352134)
