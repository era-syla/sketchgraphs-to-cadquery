import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.04188, 0.06249).lineTo(-0.01247, 0.06249).lineTo(-0.01247, -0.05771).lineTo(-0.04188, -0.05771).lineTo(-0.04188, 0.06249).close()
solid=wp_sketch0.add(loop0).extrude(-0.08297607711308914)
