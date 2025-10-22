import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0635, 0.05398).lineTo(-0.0635, 0.05398).lineTo(-0.0635, -0.05398).lineTo(0.0635, -0.05398).lineTo(0.0635, 0.05398).close()
solid=wp_sketch0.add(loop0).extrude(0.07953472044132255)
